from sqlalchemy.orm import Session
from .. import schemas, models
from fastapi import status, HTTPException

def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body = request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'Message': f'Blog with id {id} not found'})
    else:
        blog.delete(synchronize_session=False)
        db.commit()
        return {'Message': f'The blog with id {id} was deleted successfully!'}


def update(id: int, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'Message': f'Blog with id {id} not found'})
    else:
        blog.update({'title': request.title, 'body': request.body})
        db.commit()
        return {'Message': f'Blog with id {id} has been updated'}


def show(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f'Blog with id {id} not found')
        # response.status_code = status.HTTP_404_NOT_FOUND
    else:
        return blog







